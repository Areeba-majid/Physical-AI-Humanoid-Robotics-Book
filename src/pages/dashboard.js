import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

function Dashboard() {
  return (
    <Layout title="Dashboard" description="AI Textbook Platform Dashboard">
      <div className="container margin-vert--lg">
        <div className="row">
          <div className="col col--6 col--offset-3">
            <h1 className="hero__title">Student Dashboard</h1>
            <p className="hero__subtitle">Welcome to your personalized learning dashboard!</p>
            
            <div className="margin-vert--lg">
              <h2>Your Progress</h2>
              <div class="card">
                <div class="card__body">
                  <h3>Learning Modules</h3>
                  <p>You have completed 0 out of 10 modules.</p>
                  
                  <h3>Recent Activity</h3>
                  <p>No activity yet. Start exploring the textbook or taking quizzes!</p>
                  
                  <div className="margin-vert--md">
                    <Link className="button button--primary button--lg" to="/docs/intro">
                      Start Learning
                    </Link>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="margin-vert--lg">
              <h2>Quick Actions</h2>
              <div class="card">
                <div class="card__body">
                  <div className="button-group button-group--block">
                    <Link className="button button--secondary" to="/docs/textbook/chapter2">
                      Chapter 2
                    </Link>
                    <Link className="button button--secondary" to="/quiz">
                      Take Quiz
                    </Link>
                    <Link className="button button--secondary" to="/docs/ai-features/rag-chatbot">
                      AI Chatbot
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default Dashboard;