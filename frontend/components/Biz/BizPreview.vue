<template>
  <nuxt-link :to="bizlink" class="biz-preview">
    <article>
      <div
        class="biz-thumbnail"
        :style="{ backgroundImage: 'url(' + gallery + ')' }"
      ></div>
      <div class="biz-content">
        <h1>{{ title }}</h1>
        <p>{{ description }}</p>
      </div>
    </article>
  </nuxt-link>
</template>

<script>
export default {
  name: 'BizPreview',
  props: {
    id: {
      type: String,
      required: true,
    },
    isAdmin: {
      type: Boolean,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    gallery: {
      type: String,
      required: true,
    },
  },
  computed: {
    bizlink() {
      return this.isAdmin ? '/admin/' + this.id : '/biz/' + this.id
    },
  },
}
</script>

<style scoped>
.biz-preview {
  border: 1px solid #ccc;
  box-shadow: 0 2px 2px #ccc;
  background-color: white;
  width: 90%;
}

a {
  text-decoration: none;
  color: black;
}

@media (min-width: 850px) {
  .biz-preview {
    width: 400px;
    margin: 10px;
  }
}

.biz-thumbnail {
  width: 100%;
  height: 200px;
  background-position: center;
  background-size: cover;
}

.biz-content {
  padding: 10px;
  text-align: center;
}

a:hover .biz-content,
a:active .biz-content {
  background-color: #ccc;
}
</style>
