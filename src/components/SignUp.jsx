import { createUserWithEmailAndPassword } from "firebase/auth";
import React, { useState } from "react";
import { auth } from "./FirebaseAuth";

const SignUp = props => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const signUp = (e) => {
    e.preventDefault();
    createUserWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        console.log(userCredential);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="sign-up">
      <form onSubmit={signUp}>
        <h1>Create Account</h1>
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
          Sign Up
        </button>
      </form>
      <div className="in-out">
        <p>
          Already have an account?{" "}
          <a href="/SignIn" className="animate-check">
            Log In
          </a>
        </p>
      </div>
    </div>
  );
};

export default SignUp;