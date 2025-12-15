

import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import styles from './index.module.css';

function HeroSection() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <section className={styles.heroWrapper}>
      <div className={clsx('container', styles.heroGrid)}>
        
        {/* LEFT CONTENT */}
        <div className={styles.heroContent}>
          <Heading as="h1" className={styles.heroTitle}>
            {siteConfig.title}
          </Heading>

          <p className={styles.heroSubtitle}>
            {siteConfig.tagline}
          </p>

          <div className={styles.heroActions}>
            <Link
              className="button button--primary button--lg"
              to="/docs/intro">
              Read the Book 📖
            </Link>

            <Link
              className="button button--outline button--lg"
              to="https://github.com/Azratalib123"
              target="_blank">
              GitHub
            </Link>
          </div>
        </div>

        {/* RIGHT VISUAL */}
        <div className={styles.heroVisual}>
          <div className={styles.visualCard}>
            <span>🤖</span>
            <h3>Physical AI</h3>
            <p>Spec-driven, practical robotics knowledge</p>
          </div>
        </div>

      </div>
    </section>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={siteConfig.title}
      description={siteConfig.tagline}
    >
      <HeroSection />

      <main className={styles.mainContent}>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
