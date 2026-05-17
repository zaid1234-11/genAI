# Deployment Guide: Vercel + Groq

## 1. Prepare Locally

```bash
npm install
npm run build
```

Create `.env.local` for local testing:

```bash
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

## 2. Get a Groq API Key

1. Go to [https://console.groq.com](https://console.groq.com).
2. Open API Keys.
3. Create and copy a key.

## 3. Deploy on Vercel

1. Import the GitHub repository in Vercel.
2. Keep the default Next.js build settings.
3. Add environment variables:
   - `GROQ_API_KEY`
   - `GROQ_MODEL` optional
4. Deploy.

## 4. Verify

After deployment, open the app and generate a test post.

If generation fails, check:

- `GROQ_API_KEY` exists in the Vercel project settings.
- The key is valid in the Groq console.
- The deployment was redeployed after environment variables were added.
- Vercel function logs for the `/api/posts` route.

## Important Security Note

Use `GROQ_API_KEY`, not `NEXT_PUBLIC_GROQ_API_KEY`. Variables with `NEXT_PUBLIC_` are bundled into client-side code and can be viewed by users.
