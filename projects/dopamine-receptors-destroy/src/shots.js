// Shots file for Dopamine Receptors Short
import { ctx, C, W, H, clamp, lerp, seg, eo, eio, eob, rnd, bigText } from './core/lib.js';
import { L, Le, Wd, T } from './core/timing.js';
import * as K from './core/kit.js';

export function buildShots() {
  const S = [], CUES = [];
  const add = (o) => (S.push(o), o);
  const cue = (t, type, o = {}) => CUES.push({ t: +t.toFixed(3), type, ...o });
  const cut = (i) => (i === 0 ? 0 : L(i) - 0.08);

  // 1 · HOOK: Scrolling in bed
  {
    const st = cut(0), scrollWd = Wd('scroll', 0) - st;
    add({ id: 'S01', at: st, cam: [540, 820], note: 'man in bed scrolling phone',
      draw(lt) {
        K.room();
        const arm = K.armPose(K.ARM.down, K.ARM.mouth, 0.4);
        const shocked = lt > scrollWd;
        K.man({ x: 540, y: 1180, s: 1.6, arm, mouth: shocked ? 'o' : 'flat', eyes: shocked ? 'wide' : 'n', brow: shocked ? 1 : 0 });
        if (lt > scrollWd) bigText('SCROLL!', 830, 560, 92, C.red, -0.18, eob(seg(lt, scrollWd, scrollWd + 0.15)));
        K.shockLines(540, 625, 300, shocked ? clamp((lt - scrollWd) * 5) : 0);
      } });
    cue(st + 0.3, 'pop', { gain: 0.6 }); cue(st + scrollWd, 'boing', { gain: 0.5 });
  }

  // 2 · CALM BRAIN: alpha wave state
  {
    const st = cut(1), calmWd = Wd('calm', 1) - st;
    add({ id: 'S02', at: st, cam: [540, 1050], zoom: 0.3, note: 'xray calm waves',
      draw(lt, d, t) {
        K.xray(t);
        K.man({ x: 540, y: 1120, s: 1.5, xray: true, mouth: 'smile', eyes: 'n', brow: 0 });
      } });
    cue(st, 'whoosh');
  }

  // 3 · 200% DOPAMINE SPIKE
  {
    const st = cut(2), spikeWd = Wd('spike', 2) - st;
    add({ id: 'S03', at: st, cam: [540, 900], note: 'dopamine spike meter',
      draw(lt, d, t) {
        K.xray(t);
        const bob = Math.sin(lt * 2.4) * 18;
        K.man({ x: 540, y: 1120, s: 1.5, xray: true, mouth: 'o', eyes: 'wide', brow: 1, pulse: Math.abs(Math.sin(lt * 6)) });
        if (lt > spikeWd) bigText('+200% DOPAMINE', 540, 600, 80, C.yellow, 0, eob(seg(lt, spikeWd, spikeWd + 0.2)));
      } });
    cue(st, 'whoosh'); cue(st + spikeWd, 'sizzle', { dur: 1.0 });
  }

  // 4 · RECEPTORS BURNED
  {
    const st = cut(3), protWd = Wd('protect', 3) - st;
    add({ id: 'S04', at: st, cam: [540, 820], note: 'receptors shutdown',
      draw(lt, d, t) {
        K.insideStomach(t);
        bigText('RECEPTORS BURNING', 540, 800, 72, C.red, 0, 1);
      } });
    cue(st, 'whoosh'); cue(st + 0.3, 'slam');
  }

  // 5 · STUDY & WORK PAINFUL
  {
    const st = cut(4);
    add({ id: 'S05', at: st, cam: [540, 820], note: 'painful face',
      draw(lt) {
        K.room();
        K.man({ x: 540, y: 1180, s: 1.6, mouth: 'frown', eyes: 'closed', brow: 1 });
        bigText('NO MOTIVATION', 540, 500, 84, C.red, 0, 1);
      } });
    cue(st, 'whoosh'); cue(st + 0.5, 'thud');
  }

  // 6 · MYTH BUSTED
  {
    const st = cut(5), mythWd = Wd('myth', 5) - st;
    add({ id: 'S06', at: st, cam: [540, 820], note: 'myth busted',
      draw(lt) {
        K.room();
        K.man({ x: 540, y: 1180, s: 1.6, mouth: 'smirk', eyes: 'n', brow: 0 });
        if (lt > mythWd) bigText('TOTAL MYTH!', 540, 600, 96, C.yellow, -0.05, eob(seg(lt, mythWd, mythWd + 0.2)));
      } });
    cue(st, 'whoosh'); cue(st + mythWd, 'pop');
  }

  // 7 · RESET IN 48 HOURS
  {
    const st = cut(6);
    add({ id: 'S07', at: st, cam: [540, 820], note: 'reset 48h',
      draw(lt) {
        K.room();
        K.man({ x: 540, y: 1180, s: 1.6, mouth: 'smile', eyes: 'wide' });
        bigText('48 HOURS RESET', 540, 600, 86, C.cyan, 0, 1);
      } });
    cue(st, 'whoosh');
  }

  // 8 · WAIT 30 MINUTES
  {
    const st = cut(7);
    add({ id: 'S08', at: st, cam: [540, 820], note: 'wait 30 mins',
      draw(lt) {
        K.room();
        K.man({ x: 540, y: 1180, s: 1.6, arm: K.ARM.wave, mouth: 'smile', eyes: 'n' });
        bigText('WAIT 30 MINS', 540, 500, 90, C.yellow, 0, 1);
      } });
    cue(st, 'whoosh');
  }

  // 9 · FOCUS DOUBLE
  {
    const st = cut(8);
    add({ id: 'S09', at: st, cam: [540, 820], note: 'double focus',
      draw(lt) {
        K.room();
        K.man({ x: 540, y: 1180, s: 1.6, mouth: 'grin', eyes: 'wide' });
        bigText('2X FOCUS!', 540, 550, 110, C.cyan, 0, 1);
      } });
    cue(st, 'whoosh'); cue(st + 0.5, 'pop');
  }

  return { shots: S, cues: CUES };
}
