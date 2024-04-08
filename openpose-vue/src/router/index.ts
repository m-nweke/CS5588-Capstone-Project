import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Login from "@/views/auth/Login.vue";
import Registration from "@/views/auth/Registration.vue";
import Dashboard from "@/views/Dashboard.vue";
import { auth } from '@/main';
import { onAuthStateChanged } from 'firebase/auth';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Registration
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      meta: {
        requiresAuth: true,
      }
    },
  ]
})

const getCurrentUser = () => {
  return new Promise ((resolve, reject) => {
    // @ts-ignore
    const removeListener = onAuthStateChanged(
        auth,
        (user) => {
          removeListener();
          resolve(user)
        },
        reject
    );
  })
}
router.beforeEach(async (to, from, next) => {
  // If route requires authentication
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (await getCurrentUser()) {
      next();
    } else {
      alert('You must be logged in to see this page!');
      next({ name: 'login' }); // Redirect to the login page if no user
    }
  } else {
    next(); // Allow access to non-authenticated routes
  }
});

export default router
