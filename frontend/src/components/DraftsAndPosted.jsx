import { createSignal, onMount } from "solid-js";
import TweetCard from "./TweetCard";

export default function DraftsAndPosted() {
  const [tweets, setTweets] = createSignal([]);

  async function fetchTweets() {
    const res = await fetch("http://localhost:8000/tweets");
    const data = await res.json();
    setTweets(data);
  }

  onMount(fetchTweets);

  return (
    <div>
      <h2>All Tweets</h2>
      {tweets().map(tweet => (
        <TweetCard
          id={tweet.id}
          content={tweet.content}
          status={tweet.status}
          refresh={fetchTweets}
        />
      ))}
    </div>
  );
}
