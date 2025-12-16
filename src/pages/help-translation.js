import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

function HelpTranslation() {
  return (
    <Layout title="Help Translate" description="Help translate the AI Textbook Platform to other languages">
      <div className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset-2">
            <h1 className="hero__title">Help Translate Our Content</h1>
            <p className="hero__subtitle">Join our community in making education accessible to everyone, everywhere</p>
            
            <div className="margin-vert--lg">
              <div class="card">
                <div class="card__body">
                  <h3>Why Contribute Translations?</h3>
                  <p>
                    By contributing translations, you're helping make our AI and robotics education content 
                    accessible to learners around the world who speak different languages. Your efforts will 
                    directly impact students who might otherwise face language barriers to high-quality STEM education.
                  </p>
                </div>
              </div>
            </div>
            
            <div className="margin-vert--lg">
              <div class="card">
                <div class="card__body">
                  <h3>How to Contribute</h3>
                  <ol>
                    <li>Sign up as a volunteer translator on our <a href="https://github.com/your-repo/translations">GitHub repository</a></li>
                    <li>Choose a language you're fluent in</li>
                    <li>Pick a section of content to translate</li>
                    <li>Submit your translations for review</li>
                  </ol>
                  
                  <p>Currently translating to: Urdu, Spanish, French, German, Japanese</p>
                </div>
              </div>
            </div>
            
            <div className="margin-vert--lg">
              <div class="card">
                <div class="card__body">
                  <h3>Available Languages</h3>
                  <ul>
                    <li>Urdu - 40% complete</li>
                    <li>Spanish - 20% complete</li>
                    <li>French - 10% complete</li>
                    <li>German - 5% complete</li>
                    <li>Japanese - 2% complete</li>
                  </ul>
                  
                  <div className="margin-vert--md">
                    <Link className="button button--primary button--lg" to="https://github.com/your-repo/translations">
                      Start Contributing
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

export default HelpTranslation;