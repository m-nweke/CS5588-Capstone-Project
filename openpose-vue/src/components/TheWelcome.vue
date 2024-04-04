<script setup lang="ts">
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>
  <div class="container">
    <div class="welcome-section">
      <h1>Welcome to OpenPosture</h1>
      <p class="description">OpenPosture is a revolutionary app designed to transform your posture habits, offering a comprehensive suite of features tailored to meet your needs. With OpenPosture, you’ll experience personalized guidance and real-time feedback to correct poor seated posture, enhance spinal alignment, and alleviate discomfort.</p>
    </div>
    <div class="steps">
      <WelcomeItem>
        <template #icon>
          <DocumentationIcon />
        </template>
        <template #heading>Dataset Preparation</template>

        A curated dataset of diverse seated posture images underpins model training, focusing on critical body parts like the back, hands, neck, and feet for accurate posture recognition.
      </WelcomeItem>

      <WelcomeItem>
        <template #icon>
          <ToolingIcon />
        </template>
        <template #heading>Posture Analysis</template>

        The system precisely identifies key posture points and assesses posture alignment, pinpointing specific areas needing improvement.
      </WelcomeItem>

      <WelcomeItem>
        <template #icon>
          <EcosystemIcon />
        </template>
        <template #heading>Personalized Feedback</template>

        Based on posture analysis, personalized correction recommendations are generated and delivered through this Vue.js UI, powered by Flask and Firebase, offering users an intuitive and seamless experience in improving their posture.
      </WelcomeItem>

      <WelcomeItem>
        <template #icon>
          <CommunityIcon />
        </template>
        <template #heading>Feedback Mechanism</template>

        An immediate feedback mechanism provides visual cues directly to the user, suggesting posture adjustments, prompts breaks, or offering specific exercises designed to mitigate any detected posture issues, fostering an interactive and beneficial user experience.
      </WelcomeItem>
    </div>
  </div>
</template>

<style scoped>
.welcome-section {
  text-align: center;
  margin-bottom: 40px;
  padding-left: 40px; /* Add left padding to the welcome section */
}

.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.description {
  margin-bottom: 40px;
}

.steps {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}
</style>
