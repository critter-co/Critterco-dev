import Vue from 'vue'

import AppButton from "@/components/UI/AppButton";
import AppControlInput from "@/components/UI/AppControlInput";
import VueGeolocation from 'vue-browser-geolocation';

Vue.use(VueGeolocation);


Vue.component('AppButton', AppButton)
Vue.component('AppControlInput', AppControlInput)
