import TweetForm from "./components/TweetForm";
import DraftsAndPosted from "./components/DraftsAndPosted";

export default function App() {
  return (
    <div style={{ padding: "1rem", fontFamily: "sans-serif" }}>
      <h1>Tweet Generator Bot</h1>
      <TweetForm />
      <hr style={{ margin: "2rem 0" }} />
      <DraftsAndPosted />
    </div>
  );
}
