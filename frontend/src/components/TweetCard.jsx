export default function TweetCard(props) {
  async function postTweet() {
    const res = await fetch(`http://localhost:8000/post-tweet/${props.id}`, {
      method: "POST"
    });
    if (res.ok) {
      alert("Tweet posted!");
      props.refresh();
    }
  }

  return (
    <div style={{ border: "1px solid #ccc", padding: "1rem", marginBottom: "1rem" }}>
      <p>{props.content}</p>
      <small>Status: {props.status}</small>
      {props.status === "draft" && (
        <div>
          <button onClick={postTweet}>Post</button>
        </div>
      )}
    </div>
  );
}
