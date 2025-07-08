import { createSignal } from "solid-js";

export default function TweetForm() {
  const [prompt, setPrompt] = createSignal("");
  const [tweet, setTweet] = createSignal("");
  const [status, setStatus] = createSignal("");

  async function generateTweet() {
    setStatus("Generating...");
    try {
      const res = await fetch("http://localhost:8000/generate-tweet", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: prompt() })
      });

      if (!res.ok) {
        const error = await res.json();
        throw new Error(error.detail || "Failed to generate tweet");
      }

      const data = await res.json();
      setTweet(data.content);
      setStatus("Tweet generated ✅");
    } catch (err) {
      setStatus(`Error: ${err.message}`);
      console.error(err);
    }
  }

  async function saveDraft() {
    try {
      const res = await fetch("http://localhost:8000/save-draft", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: tweet(), status: "draft" })
      });

      await res.json();
      setStatus("Saved as Draft ✅");
    } catch (err) {
      setStatus("Error saving draft ❌");
      console.error(err);
    }
  }

  async function postTweet() {
    setStatus("Posting...");
    try {
      // Save first
      const saveRes = await fetch("http://localhost:8000/save-draft", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: tweet(), status: "draft" })
      });

      if (!saveRes.ok) throw new Error("Failed to save tweet");

      const { id } = await saveRes.json();

      // Post to Twitter Clone
      const postRes = await fetch(`http://localhost:8000/post-tweet/${id}`, {
        method: "POST"
      });

      if (!postRes.ok) throw new Error("Failed to post tweet to Twitter Clone");

      setStatus("Tweet posted successfully ✅");
    } catch (err) {
      setStatus(`Post failed ❌: ${err.message}`);
      console.error(err);
    }
  }

  return (
    <div>
      <textarea
        rows="3"
        style={{ width: "100%", marginBottom: "0.5rem" }}
        placeholder="Enter tweet idea"
        value={prompt()}
        onInput={(e) => setPrompt(e.target.value)}
      />
      <button onClick={generateTweet}>Generate Tweet</button>
      {tweet() && (
        <>
          <p><strong>Generated Tweet:</strong> {tweet()}</p>
          <button onClick={saveDraft}>Save as Draft</button>
          <button onClick={postTweet} style={{ marginLeft: "0.5rem" }}>
            Post Now
          </button>
        </>
      )}
      <p>{status()}</p>
    </div>
  );
}
