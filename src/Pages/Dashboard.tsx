import { Link } from "react-router-dom";
import { Button } from "../components/ui/button";
import { placehold } from "../constants";

const Dashboard = () => {
  return (
    <div className="h-screen w-full">
      <div className="w-full mx-auto flex flex-col mt-28 gap-10 items-center justify-center">
        <h1 className="font-semibold text-2xl">Welcome to Colauncha</h1>
        <p>Colaucha's Dashboard helps manage your queries</p>
        <div className="flex flex-col lg:flex-row gap-20">
          <aside className="flex flex-col items-center justify-center gap-4">
            <Button className="bg-red-400 hover:bg-red-500">logout</Button>
            <img src={placehold} alt="" className="w-40 h-40 rounded-full border" />
          </aside>
          <main className="flex flex-col gap-10">
            <div className="flex gap-20 items-center justify-center">
              <div className="">
                <Button className="bg-blue-700 hover:bg-blue-400">
                  <Link to="/talent-request">Request As a Talent</Link>
                </Button>
              </div>
              <div className="">
                <Button className="bg-green-600 hover:bg-green-300">
                  <Link to="/project-request">Request As a Talent</Link>
                </Button>
              </div>
            </div>
          </main>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
