<template>
  <div class="todo">
    {{ text }}
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class Todo extends Vue {}
</script>

<style scoped lang="scss">
</style>
