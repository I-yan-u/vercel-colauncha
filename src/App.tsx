import "./App.css";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Header from "./sections/Header";
import Hero from "./sections/Hero";
import TalentRequest from "./Pages/TalentRequest";
import Testimonial from "./sections/Testimonial";
import Footer from "./sections/Footer";
import FormRequest from "./sections/FormRequest";
import About from "./sections/About";
import Contact from "./sections/Contact";
import Mvp from "./sections/Mvp";

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
              <About />
              <Mvp/>
              <FormRequest/>
              <Testimonial />
              <Contact/>
            </>
          }
        />
        <Route path="/about" element />
        <Route
          path="/talent-request"
          element={
            <>
              <TalentRequest />
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
