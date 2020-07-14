<template>
  <div>
    <h1>Bizs Page</h1>
    <p v-if="$fetchState.pending">Getting Bizs...</p>
    <p v-else-if="$fetchState.error">Error while getting bizs: {{ $fetchState.error.message }}</p>
    <ul v-else>
      <li v-for="biz of bizs" :key="biz.id">
        <n-link :to="`/biz/${biz.id}`">{{ biz.title }}</n-link>
      </li>
    </ul>
    <nuxt keep-alive :keep-alive-props="{ max: 10 }" />
  </div>
</template>

<script>
import axios from 'axios'
export default {
   data() {
    return {
      bizs: []
    };
  },
  async fetch() {
    const { data } = await axios.get(
      `http://localhost/api/biz`
    );
    // `bizs` has to be declared in data()
    this.bizs = data;
  }
}
</script>


