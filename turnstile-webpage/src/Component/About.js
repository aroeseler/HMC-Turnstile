import React from 'react';

export default class Home extends React.Component {
    render() {
        return (
            <div className="app">
              <header>
                  <div className="wrapper">
                    <h1>Turnstile</h1>
                  </div>
              </header>
            <div>
              <section className="display-about">
                <h1>About Turnstile:</h1>
                <h3>Turnstile is a traffic tool that provides users information about the Hoch-Shanahan Dining Commons at Harvey Mudd College.</h3><br/>
                <h3>Created as part of a project for a Software Development class, Turnstile uses object tracking and React to obtain and display information relevant to the dining hall.</h3><br/>
                <h3>We use a Raspberry Pi 4 and an Intel Neural Compute Stick to detect people walking in or out of the Hoch, then push that information to a Firebase database.</h3><br/>
                <h3>Then we use React to create a webpage and process the data. The webpage is remote hosted using Firebase Hosting.</h3>
                <br/><br/><br/>
                <h3>Turnstile was created by Andreas Roeseler, Aaron Trujillo, and Daniel Sealand, HMC '21</h3><br/>
                
              </section>
            </div>
            </div>
        );
    }
}