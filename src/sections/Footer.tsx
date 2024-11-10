import { useEffect } from "react";
import { facebook, instagram, linkedin, scrollup, youtube } from "../constants";
import { Link } from "react-router-dom";




const Footer = () => {
  const ScrollToTop =()=>{
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

    useEffect(() => {
      ScrollToTop() 
    }, []);

  return (
    <div className="mt-20 relative" id="footer-section">
      <button className="absolute right-10 lg:right-24 top-[-22px] cursor-pointer w-14 h-14" onClick={ScrollToTop}>
        <img src={scrollup} alt="scrollUp_func"  />
      </button>
      <div className="h-[329px] w-full bg-[#fec91b]">
        <div className="w-[90%] mx-auto py-24 flex justify-center flex-col gap-16 relative">
          <div className="flex flex-col items-center lg:items-start">
            <h2 className="text-[32px] lg:text-[60px] font-[700]">
              Follow our latest news
            </h2>
            <div className="flex gap-14 items-center">
              <Link
                to="/"
                className="bg-[#ffee00] rounded-full w-12 h-12 flex items-center justify-center"
              >
                <img src={facebook} alt="" />
              </Link>
              <Link
                to="/"
                className="bg-[#ffee00] rounded-full w-12 h-12 flex items-center justify-center"
              >
                <img src={youtube} alt="" />
              </Link>
              <Link
                to="/"
                className="bg-[#ffee00] rounded-full w-12 h-12 flex items-center justify-center"
              >
                <img src={linkedin} alt="" />
              </Link>
              <Link
                to="/"
                className="bg-[#ffee00] rounded-full w-12 h-12 flex items-center justify-center"
              >
                <img src={instagram} alt="" />
              </Link>
            </div>
          </div>
          <div className="lg:text-xl flex justify-center lg:absolute bottom-10 right-6">
            copyright &copy; 2024 Designed by Colauncha
          </div>
        </div>
      </div>
    </div>
  );
};

export default Footer;
