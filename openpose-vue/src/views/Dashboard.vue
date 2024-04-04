<template>
Hello {{ name }}
</template>

<style scoped>

</style>

<script setup lang="ts">
import { auth } from '@/main';

const user = auth.currentUser;
const name = auth.currentUser?.displayName
</script>
