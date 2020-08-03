import Cookie from 'js-cookie';

const local = "http://localhost";

export const state = () => {
  biz: []
}

export const mutations =
{
  getBiz(state, bizes) {
    state.biz = bizes
  },
  addBiz(state, biz) {
    state.biz.push(biz)
  },
}

export const actions =
{
  createBiz(vuexContext, bizData) {
    console.log('given coord: ' + bizData.loc)
    const auth = Cookie.get('CAT');
    let createBizUrl = `${local}/api/biz/`
    return this.$axios.$post(createBizUrl, {
      title: bizData.title,
      description: bizData.description,
      address: bizData.address,
      city: bizData.city,
      phone: bizData.phone,
      phone2: bizData.phone2,
      location: {
        type: "Point",
        coordinates: [
          bizData.loc.lng,
          bizData.loc.lat
        ]
      },
      website: bizData.website,
      instagram: bizData.instagram,
      telegram: bizData.telegram
    }, { headers: { 'Authorization': `Bearer ${auth}` } }).then(res => {
      console.log(res);
    }).catch(e => {
      console.log(e)
    })
  },
}

export const getters =
{
  loadedBizs(state) {
    return state.biz
  },
}