import Task from "./components/Task";
import LevelBar from "./components/LevelBar";

function App() {
  return (
    <>
      <h1 className="text-4xl text-center mx-4 mt-6 mb-2">Toodles!</h1>
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
