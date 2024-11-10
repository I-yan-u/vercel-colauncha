import { Button } from "../components/ui/button";
import {hiw_1, hiw_2, hiw_3, hiw_4 } from "../constants";

const About = () => {
  return (
    <div className="w-full min-h-screen mt-28 mb-12 " id="about-section">
      <div className="w-[90%] lg:w-[85%] mx-auto flex flex-col-reverse justify-between lg:flex-row ">
        <div className="my-6 grid lg:grid-rows-2  p-8 lg:w-[50%] gap-4 justify-center lg:justify-start ">
         <div className="grid grid-cols-2 gap-4 relative">
          <p>Exploratory Call</p>
          <p>Talents Match</p>
          <img src={hiw_3} alt="" className="h-[250px] lg:absolute top-[25px] left-[300px] "/>
          <img src={hiw_1} alt="" className="h-[250px] lg:absolute top-0 left-0 " />
         </div>
         <div className="grid grid-cols-2 gap-4 relative">
          <p>Build & Test</p>
          <p>MVP Launch</p>
          <img src={hiw_4} alt="" className="h-[250px] lg:absolute top-[60px] left-[300px]"/>
          <img src={hiw_2} alt="" className="h-[250px]" />
         </div>
        
        </div>
        <div className="flex flex-col justify-center items-center lg:w-[50%] lg:justify-start lg:items-start ">
          <h2 className="text-[45px] font-bold ">How it works</h2>
          <div className="flex flex-col gap-8">
            <p className="text-[25px] text-center lg:text-start">
              Your Path to a Fully-Developed MVP, Simplified
            </p>
            <div className="text-[25px] text-center lg:text-start font-[400] lg:w-[400px] flex flex-col gap-10">
              <p>With Colauncha, you’re not just building a product—you’re
              partnering for success.</p>
                <span>Book your talents to get started.</span>
            </div>
           <div className="flex justify-center lg:justify-start ">
           <Button className="w-full sm:w-[50%] bg-[#3783ff] rounded-xl h-12 text-white font-bold text-xl hover:bg-blue-600">
              Book here
            </Button>
           </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;
