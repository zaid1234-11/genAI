# AI Social Media Post Generator

A Next.js app that uses the Groq API to turn a rough idea into a polished social media caption with hashtags.

## Features

- Generate posts for Instagram, X, Facebook, LinkedIn, and TikTok.
- Choose from excited, professional, casual, funny, and inspirational tones.
- Copy generated posts directly from the result panel.
- Server-side API route keeps your Groq key out of the browser bundle.

## Tech Stack

- Next.js 14
- React 18
- TypeScript
- Groq SDK

## Local Setup

Install dependencies:

```bash
npm install
```

Create `.env.local` in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

Run the app:

```bash
npm run dev
```

Open `http://localhost:3000`.

## API

The generator calls `POST /api/posts` with:

```json
{
  "topic": "Launching a limited edition eco-friendly sneaker line",
  "platform": "Instagram",
  "tone": "Excited"
}
```

The route validates inputs, calls Groq with `GROQ_API_KEY`, and returns:

```json
{
  "success": true,
  "post": "Generated caption..."
}
```

## Deployment

On Vercel or another host, add these environment variables:

- `GROQ_API_KEY`
- `GROQ_MODEL` optional, defaults to `llama-3.3-70b-versatile`

Do not use `NEXT_PUBLIC_GROQ_API_KEY`; public variables are exposed to the browser.
