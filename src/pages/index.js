import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/Homepage/Features';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Get Started
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="An interactive educational platform with AI-powered features">
      <HomepageHeader />
      <main>
        <section className={styles.features}>
          <div className="container padding-horiz--md">
            <div className="row">
              <div className="col col--4">
                <h2>AI-Powered Learning</h2>
                <p>Experience education enhanced by artificial intelligence that adapts to your learning style.</p>
              </div>
              <div className="col col--4">
                <h2>Interactive Content</h2>
                <p>Engage with dynamic textbooks, quizzes, and hands-on exercises to reinforce your knowledge.</p>
              </div>
              <div className="col col--4">
                <h2>Personalized Experience</h2>
                <p>Content tailored to your pace, preferences, and learning objectives.</p>
              </div>
            </div>
          </div>
        </section>
        
        <section className="padding-vert--lg">
          <div className="container text--center">
            <h2>About This Textbook</h2>
            <p>An interactive textbook platform for AI-native Physical AI & Humanoid Robotics</p>
            <div className="margin-vert--lg">
              <Link className="button button--primary button--lg" to="/docs/intro">
                Explore Chapters
              </Link>
              <Link className="button button--secondary button--lg margin-left--sm" to="/quiz">
                Take a Quiz
              </Link>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}