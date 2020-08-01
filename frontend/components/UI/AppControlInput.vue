<template>
  <div :class="groupClass">
    <input v-bind="$attrs" :class="inputClass" :value="value"  @input="$emit('input', $event.target.value)" required />
    <label for="name" class="form__label">
      <slot />
    </label>
  </div>
</template>

<script>
export default {
  namme: "AppControlInput",
  inheritAttrs: false,
  props: {
    value: {
      type: String,
      default: "",
    },
    inputClass: {
      type: String,
      default: "",
    },
    groupClass: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
</style>