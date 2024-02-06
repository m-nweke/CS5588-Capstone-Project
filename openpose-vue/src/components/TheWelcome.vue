<script setup lang="ts">
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Integration</template>

    Our first steps includes following
    <a href="https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/" target="_blank" rel="noopener">this example</a>
    to get our backend and frontend connected.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Create Dataset</template>

    Next we will create our own dataset by taking pictures with a number of different postures.
    <br />
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <EcosystemIcon />
    </template>
    <template #heading>Import data to firebase</template>

    The next step involves using firebase docs to get the dataset into the firestore
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>Serve data to frontend</template>

    From there we need to create some HTTPS routes that can serve the data to the frontend as well as submit data from the frontend to the database.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading>Start model development</template>

    Once this is done, we can work on feeding the data to the model
  </WelcomeItem>
</template>
