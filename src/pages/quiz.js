import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

function QuizPage() {
  return (
    <Layout title="Quizzes" description="Practice quizzes for AI Textbook Platform">
      <div className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset-2">
            <h1 className="hero__title">Interactive Quizzes</h1>
            <p className="hero__subtitle">Test your knowledge with our AI-generated quizzes tailored to each chapter</p>

            <div className="margin-vert--lg">
              <div class="card">
                <div class="card__body">
                  <h3>Chapter Quizzes</h3>
                  <ul class="margin-vert--md">
                    <li><Link to="/docs/quizzes/chapter1-quiz">Chapter 1: Introduction to AI</Link></li>
                    <li><Link to="/docs/quizzes/chapter2-quiz">Chapter 2: Foundations of Robotics</Link></li>
                    <li><Link to="/docs/quizzes/chapter3-quiz">Chapter 3: Physical AI Systems</Link></li>
                    <li><Link to="/docs/quizzes/chapter4-quiz">Chapter 4: Humanoid Robotics</Link></li>
                  </ul>

                  <h3>Advanced Topics</h3>
                  <ul class="margin-vert--md">
                    <li><Link to="/docs/quizzes/midterm">Midterm Assessment</Link></li>
                    <li><Link to="/docs/quizzes/final">Final Examination</Link></li>
                  </ul>
                </div>
              </div>
            </div>

            <div className="margin-vert--lg">
              <h2>How It Works</h2>
              <div class="card">
                <div class="card__body">
                  <p>Our AI generates dynamic quizzes based on the content you've studied, adapting to your learning pace and style.</p>
                  <p>Get instant feedback and personalized recommendations for areas that need improvement.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default QuizPage;