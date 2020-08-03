export default function (context) {
    context.store.dispatch('register/checkAuth', context.req);
    console.log('checking Auth from middleware')
}