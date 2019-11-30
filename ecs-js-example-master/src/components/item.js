export const Item = {};

export const ParentEffect = {
  properties: {
    effects: {}
  },
  multiset: true
};

export const EffectsFrom = {
  properties: {
    effects: '<ComponentArray>',
    slot: '<Component>',
    item: '<Entity>'
  },
  multiset: true
}

export const Equipable = {
  properties: {
    slotType: 'legs'
  }
}

export const Unidentified = {};

export const Weapon = {
  properties: {
    hit: '',
    dmg: '',
  }
}
