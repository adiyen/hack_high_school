from positions import PointGaurd, ShootingGaurd, SmallForward, PowerForward, Center

def main():
    playbook = {
        "pg": "I'll dribble penentrate",
        "sg": "I'll cut to the corner",
        "sf": "I'll run to the wing",
        "pf": "I'll set the second pick",
        "c": "I'll set the first pick"
    }

    pg = PointGaurd(playbook)
    pg.run_play("pg")

    sg = ShootingGaurd(playbook)
    sg.run_play("sg")

    sf = SmallForward(playbook)
    sf.run_play("sf")

    pf = PowerForward(playbook)
    pf.run_play("pf")

    c = Center(playbook)
    c.run_play("c")

    c.run_play("cf")


if __name__ =="__main__":
    main()