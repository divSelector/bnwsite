from dataclasses import dataclass

@dataclass
class Enemy:
    name: str
    hp: int
    mp: int
    exp: int
    gp: int
    weak: str
    block: str
    resist: str
    status: str


@dataclass
class Skill:
    name: str
    targeting: str
    power: str
    evade: str
    damage: str
    description: str

@dataclass
class RageAction:
    name: str
    two_thirds_odds: str
    two_thirds_targeting: str
    two_thirds_power: str
    two_thirds_descrip: str
    one_third_odds: str
    one_third_targeting: str
    one_third_power: str
    one_third_descrip: str


@dataclass
class RageProp:
    name: str
    weakness: str
    block_absorb: str
    resistance: str
    innate: str


@dataclass
class SlotSkill:
    name: str
    targeting: str
    power: str
    description: str


@dataclass
class Weapon:
    name: str
    value: str
    attack: str
    evade: str
    m_evade: str
    stat_boost: str
    equip: str
    description: str


@dataclass
class Item:
    name: str
    value: str
    description: str


@dataclass
class Legend:
    name: str
    description: str


@dataclass
class DefenseEquip:
    name: str
    value: str
    defense: str
    m_defense: str
    evade: str
    m_evade: str
    stat_boost: str
    equip: str
    description: str
