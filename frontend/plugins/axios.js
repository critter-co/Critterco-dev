
export default function ({ $axios, app }) {
    const cookieCsrf = app.$cookies.get('csrftoken')

    $axios.onRequest((config) => {
        config.headers.common['csrftoken'] = cookieCsrf
        console.log(cookieCsrf)
    })
}
