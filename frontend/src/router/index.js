import Vue from 'vue'
import Router from 'vue-router'
import ItemList from '@/components/ItemList'
import ItemRegister from '@/components/ItemRegister'
import DetailDemo from '@/components/DetailDemo'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/list',
      name: 'ItemList',
      component: ItemList,
      children:[
      {
         path:'detail/:id',
         component : DetailDemo
      }
      ]
    },
    {
      path: '/register',
      name: 'ItemRegister',
      component: ItemRegister
    },
    {
      path:'/',
      redirect:'/list'
    }

  ]
})
