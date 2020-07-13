export default function (context) {
    context.store.dispatch('checkAuth', context.req);
    console.log('checking Auth from middleware')
}