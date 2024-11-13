import "./App.css";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Header from "./sections/Header";
import Hero from "./sections/Hero";
import TalentRequest from "./Pages/TalentRequest";
import Testimonial from "./sections/Testimonial";
import Footer from "./sections/Footer";
import FormRequest from "./sections/FormRequest";
import About from "./Pages/About";
import Contact from "./sections/Contact";
import Mvp from "./sections/Mvp";
import Auth from "./auth/Auth";
import JoinAsTalent from "./sections/JoinAsTalent";
import BookTalent from "./sections/BookTalent";
import OurTeam from "./Pages/OurTeam";

function App() {
  return (
    <div className="app">
    <Router>
      <Header />
      <Routes>
        <Route
          path="/"
          element={
            <>
              <Hero />
              <BookTalent />
              <Mvp/>
              <JoinAsTalent/>
              <Testimonial />
              <Contact/>
            </>
          }
        />
        <Route path="/about" element={<About/>} />
        <Route path="/our-team" element={<OurTeam/>} />
        <Route path="/contact" element={<Contact/>} />
        <Route path="/talent-request" element={<TalentRequest/>} />
        <Route path="/book-talent" element={<BookTalent/>} />
        <Route
          path="/talent-request"
          element={
            <>
              <Auth />
            </>
          }
        />
      
      </Routes>
      <Footer/>
    </Router>
    </div>
  );
}

export default App;
