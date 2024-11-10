import bg from "../assets/clients/clientsays.png";
import { client_1, client_2, client_3 } from "../constants";
// import Carousel from "../components/Carousel";

const Testimonial = () => {
  return (
    <div className="h-screen w-full mb-[4rem]" id="testimonial-section mb-28">
      <div
        className="bg-cover bg-center h-[60%]"
    mb-60    style={{ backgroundImage: `url(${bg})` }}
      >
        <div className="w-[90%] mx-auto pt-8 ">
          <h2 className="text-white  font-bold text-[20px] lg:text-[40px]">
            CLIENTS TESTIMONY
          </h2>
          <div className="pt-60 w-full">
            {/* <Carousel/> */}
            <div className="flex justify-center gap-12 overflow-hidden w-[80%] mx-auto items-center">
              <div className="flex flex-col gap-6 bg-[#ff8c0080] p-4 h-[300px] w-[300px] rounded-[20px]">
                <div className="flex items-center gap-4">
                  <img src={client_3} className="w-12 h-12 rounded-full bg-blue-800"></img>
                  <p className="text-white text-[18px] font-bold">Charles Davies</p>
                </div>
                <div>
                  <p className="pt-4 text-lg">
                    Hey! Colaucha is taking over in the ecosystem, from Nigeria to the World, thank you amazing team for a swift delivery.
                  </p>
                </div>
              </div>
            
              <div className="flex flex-col gap-6 bg-[#ff8c0080] p-4 h-[300px] w-[300px] rounded-[20px] ">
                <div className="flex items-center gap-4">
                  <img src={client_2} className="w-12 h-12 rounded-full bg-blue-800"></img>
                  <p className="text-white text-[17px] font-bold">Francis Cole</p>
                </div>
                <div>
                  <p className="pt-2 text-lg">
                    I really appreaciate this team for not taking for granted their words. Assurance and delivery are what build trust.
                  </p>
                </div>
              </div>
            
              <div className="flex flex-col gap-6 bg-[#ff8c0080] p-4 h-[300px] w-[300px] rounded-[20px] ">
                <div className="flex items-center gap-4">
                  <img src={client_1} className="w-12 h-12 rounded-full bg-blue-800"></img>
                  <p className="text-white text-[17px] font-bold">Jumoke Bello</p>
                </div>
                <div>
                  <p className="pt-2 text-lg">
                    When I first spoke Mr. Shola and his team about my pitch idea and how I intend to materialize it, their kind words were amazings! from start to finish they did it.
                  </p>
                </div>
              </div>
            

            
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Testimonial;
