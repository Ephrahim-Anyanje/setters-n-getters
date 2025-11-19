import { Greeting } from "./Greeting";
import { UserBox } from "./box";

import "../index.css";

function App() {
  return (
    <div>
      <Greeting name={Ephraim} />
      <UserBox />
    </div>
  );
}

export default App;
