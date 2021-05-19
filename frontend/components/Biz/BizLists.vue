<template>
  <section class="biz-list">
    <BizPreview
      v-for="biz in bizs"
      :key="biz.id"
      :id="biz.id"
      :is-admin="isAdmin"
      :gallery="biz.gallery"
      :title="biz.title"
      :description="biz.description"
    />
  </section>
</template>

<script>
import BizPreview from '@/components/Biz/BizPreview'
export default {
  components: {
    BizPreview,
  },
  props: {
    isAdmin: {
      type: Boolean,
      default: false,
    },
    bizs: {
      type: Array,
      required: true,
    },
  },
}
</script>

<style scoped>
.biz-list {
  display: flex;
  padding: 20px;
  box-sizing: border-box;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}
</style>
