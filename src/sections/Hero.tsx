import { Button } from "../components/ui/button";
import { hero_logo } from "../constants";


const Hero = () => {
  return (
    <div  className="w-full lg:h-screen min-h-screen" id="hero-section">
    <div className=" w-[75%] sm:w-[90%] pt-40 lg:pt-40 grid lg:grid-cols-2 mx-auto ">
      <div className="flex flex-col items-center lg:items-start lg:pl-28 justify-center lg:justify-start gap-8">
       <div>
       <h1 className="font-extrabold text-[50px] lg:text=[70px] lg:w-[420px] leading-normal text-center lg:text-start ">
          Build Your MVP in 3 Months, Zero Upfront Cost
        </h1>
        <p className="text-2xl text-center lg:w-[300px] lg:text-start lg:my-6 lg:text-3xl">
          Empowering founders with a team of experts to bring your vision to
          life.
        </p>
       </div>
       
          <div className="lg:mt-10">
          <Button className="w-[150px] h-[36px]  text-md font-[700] rounded-xl bg-[#3783ff] hover:bg-blue-600">
            Get your team now
          </Button>
         
        </div>
      </div>

      <div className="my-12 lg:my-0 flex justify-center">
       <img
          src={hero_logo}
          alt="hero_img"
          className="w-full sm:w-[100%] h-auto max-w-[500px] md:w-[700px] "
        />
      </div>
    </div>
    </div>
  );
};

export default Hero;
