"use client";

import { ChangeEvent, FormEvent, useMemo, useState } from "react";

const platforms = ["Instagram", "X", "Facebook", "LinkedIn", "TikTok"];
const tones = ["Excited", "Professional", "Casual", "Funny", "Inspirational"];

interface FormData {
  topic: string;
  platform: string;
  tone: string;
}

interface ApiResponse {
  success: boolean;
  post?: string;
  error?: string;
}

export default function Home() {
  const [formData, setFormData] = useState<FormData>({
    topic: "",
    platform: "Instagram",
    tone: "Excited",
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);

  const topicLength = formData.topic.trim().length;
  const canSubmit = topicLength >= 3 && !loading;

  const helperText = useMemo(() => {
    if (!topicLength) return "Add a product, announcement, event, or idea.";
    if (topicLength < 3) return "Give the AI a little more context.";
    return `${topicLength} characters ready for ${formData.platform}.`;
  }, [formData.platform, topicLength]);

  const handleChange = (
    event: ChangeEvent<HTMLTextAreaElement | HTMLSelectElement>
  ) => {
    const { name, value } = event.target;
    setFormData((previous) => ({ ...previous, [name]: value }));
    setCopied(false);
  };

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError(null);
    setResult(null);
    setCopied(false);

    if (formData.topic.trim().length < 3) {
      setError("Please describe your post idea in at least 3 characters.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("/api/posts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ...formData,
          topic: formData.topic.trim(),
        }),
      });

      const data = (await response.json()) as ApiResponse;

      if (!response.ok || !data.success || !data.post) {
        throw new Error(data.error || "The post could not be generated.");
      }

      setResult(data.post);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Something went wrong while generating your post."
      );
    } finally {
      setLoading(false);
    }
  };

  const copyPost = async () => {
    if (!result) return;

    await navigator.clipboard.writeText(result);
    setCopied(true);
  };

  return (
    <main className="app-shell">
      <section className="intro">
        <div>
          <p className="eyebrow">Groq powered writing assistant</p>
          <h1>Generate polished social posts in seconds.</h1>
          <p className="intro-copy">
            Turn a rough idea into a platform-ready caption with hashtags,
            tone, and structure handled for you.
          </p>
        </div>
        <div className="status-panel" aria-label="App status">
          <span className="status-dot" />
          API route ready at <strong>/api/posts</strong>
        </div>
      </section>

      <section className="workspace">
        <form className="generator-form" onSubmit={handleSubmit}>
          <div className="field">
            <div className="field-heading">
              <label htmlFor="topic">Post idea</label>
              <span>{helperText}</span>
            </div>
            <textarea
              id="topic"
              name="topic"
              value={formData.topic}
              onChange={handleChange}
              placeholder="Example: Launching a limited edition eco-friendly sneaker line this Friday."
              rows={5}
              maxLength={500}
              disabled={loading}
            />
          </div>

          <div className="field-grid">
            <div className="field">
              <label htmlFor="platform">Platform</label>
              <select
                id="platform"
                name="platform"
                value={formData.platform}
                onChange={handleChange}
                disabled={loading}
              >
                {platforms.map((platform) => (
                  <option key={platform}>{platform}</option>
                ))}
              </select>
            </div>

            <div className="field">
              <label htmlFor="tone">Tone</label>
              <select
                id="tone"
                name="tone"
                value={formData.tone}
                onChange={handleChange}
                disabled={loading}
              >
                {tones.map((tone) => (
                  <option key={tone}>{tone}</option>
                ))}
              </select>
            </div>
          </div>

          <button className="primary-button" type="submit" disabled={!canSubmit}>
            {loading ? (
              <>
                <span className="spinner" aria-hidden="true" />
                Generating
              </>
            ) : (
              "Generate post"
            )}
          </button>
        </form>

        <aside className="result-panel" aria-live="polite">
          {!result && !error && (
            <div className="empty-state">
              <p className="eyebrow">Output preview</p>
              <h2>Your generated post will appear here.</h2>
              <p>
                Keep the idea specific for better captions: audience, product,
                offer, date, or desired action all help.
              </p>
            </div>
          )}

          {error && (
            <div className="message error-message">
              <strong>Generation failed</strong>
              <p>{error}</p>
            </div>
          )}

          {result && (
            <div className="post-result">
              <div className="result-header">
                <div>
                  <p className="eyebrow">Generated post</p>
                  <h2>Ready to publish</h2>
                </div>
                <button className="secondary-button" type="button" onClick={copyPost}>
                  {copied ? "Copied" : "Copy"}
                </button>
              </div>
              <div className="post-content">{result}</div>
            </div>
          )}
        </aside>
      </section>
    </main>
  );
}
