export default async function (context) {
    if (!context.store.getters.isAuthenticated) {
        await context.redirect('/login')
    }
}