import { NextRequest, NextResponse } from "next/server";
import { Groq } from "groq-sdk";

export const runtime = "nodejs";

const allowedPlatforms = new Set(["Instagram", "X", "Facebook", "LinkedIn", "TikTok"]);
const allowedTones = new Set([
  "Excited",
  "Professional",
  "Casual",
  "Funny",
  "Inspirational",
]);

interface RequestBody {
  topic?: unknown;
  platform?: unknown;
  tone?: unknown;
}

function cleanText(value: unknown) {
  return typeof value === "string" ? value.trim() : "";
}

function getGroqErrorMessage(error: unknown) {
  if (error instanceof Error) return error.message;

  if (typeof error === "object" && error !== null && "message" in error) {
    const message = (error as { message?: unknown }).message;
    if (typeof message === "string") return message;
  }

  return "The AI provider returned an unexpected error.";
}

export async function POST(request: NextRequest) {
  const apiKey = process.env.GROQ_API_KEY;

  if (!apiKey) {
    return NextResponse.json(
      {
        success: false,
        error: "Missing GROQ_API_KEY. Add it to .env.local or your deployment environment.",
      },
      { status: 500 }
    );
  }

  let body: RequestBody;

  try {
    body = (await request.json()) as RequestBody;
  } catch {
    return NextResponse.json(
      { success: false, error: "Request body must be valid JSON." },
      { status: 400 }
    );
  }

  const topic = cleanText(body.topic);
  const platform = cleanText(body.platform);
  const tone = cleanText(body.tone);

  if (topic.length < 3) {
    return NextResponse.json(
      { success: false, error: "Please enter a more specific post idea." },
      { status: 400 }
    );
  }

  if (!allowedPlatforms.has(platform) || !allowedTones.has(tone)) {
    return NextResponse.json(
      { success: false, error: "Invalid platform or tone selected." },
      { status: 400 }
    );
  }

  const groq = new Groq({ apiKey });
  const model = process.env.GROQ_MODEL || "llama-3.3-70b-versatile";

  try {
    const completion = await groq.chat.completions.create({
      model,
      temperature: 0.7,
      max_tokens: 420,
      messages: [
        {
          role: "system",
          content:
            "You are an expert social media strategist. Write concise, practical, platform-ready posts. Do not mention that you are an AI.",
        },
        {
          role: "user",
          content: `Create one ${platform} post with a ${tone.toLowerCase()} tone for this topic: ${topic}

Include:
- A polished caption
- A clear call to action when useful
- 3 to 5 relevant hashtags

Keep the formatting clean and ready to paste.`,
        },
      ],
    });

    const post = completion.choices[0]?.message?.content?.trim();

    if (!post) {
      return NextResponse.json(
        { success: false, error: "Groq returned an empty response. Please try again." },
        { status: 502 }
      );
    }

    return NextResponse.json({ success: true, post });
  } catch (error) {
    console.error("Groq API error:", error);

    return NextResponse.json(
      {
        success: false,
        error: `Groq API request failed: ${getGroqErrorMessage(error)}`,
      },
      { status: 502 }
    );
  }
}
