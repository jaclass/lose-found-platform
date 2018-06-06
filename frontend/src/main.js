// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import qs from 'qs'
Vue.config.productionTip = false;
Vue.prototype.$ajax=axios;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

axios.interceptors.request.use((config) => {
    //在发送请求之前做某件事
    if (config.method === 'post' || config.method === 'put') {
        config.data = qs.stringify(config.data);
    }
    return config;
}, (error) => {
    _.toast("错误的传参", 'fail');
    return Promise.reject(error);
});