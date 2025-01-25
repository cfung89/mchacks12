import Task from "./components/Task";
import LevelBar from "./components/LevelBar";
import LoginButton from "./components/LoginButton";
import LogoutButton from "./components/LogoutButton";


function App() {
  return (
    <main className="column">
    <>
      <h1>Toodles!</h1>
      <h1>Auth0 Login</h1>
      <LoginButton />
      <LogoutButton />
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
    </main>
  );
}

export default App;
