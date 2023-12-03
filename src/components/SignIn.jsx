import { auth } from "./FirebaseAuth";
import { signInWithEmailAndPassword } from "firebase/auth";
import React, { useState } from "react";
import "./signIn.css";

const SignIn = props => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const signIn = (e) => {
    e.preventDefault();
    signInWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        console.log(userCredential);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="login">
    <form onSubmit={signIn}>
      <div className="field">
        <label className="label">Email</label>
        <input
          className="input"
          type="email"
          placeholder="Enter your Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div className="field">
        <label className="label">Password</label>
        <input
          className="input"
          type="password"
          placeholder="Enter your Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <button className="submit-button" type="submit">
        Log In
      </button>
    </form>
    <div className="in-out">
      <p>
        Don't have an account?{" "}
        <a href="/SignUp" className="animate-check">
          Sign Up
        </a>
      </p>
    </div>
  </div>
  );
};

export default SignIn;
