import Task from "./components/Task";
import LevelBar from "./components/LevelBar";

function App() {
  return (
    <>
      <h1>Toodles!</h1>
      <div className="container p-4">
        <Task
          taskName="Toodle!"
          xp={10}
          content="Toodle doodle doo, toodle doodle doo."
          tag="toodly"
        />
      </div>
      <LevelBar xp={30} />
    </>
  );
}

export default App;
