import * as dotenv from 'dotenv';
import * as thecamp from 'the-camp-lib';
import { getNews } from './news';
import { sendLetter } from './pigeon';

(async () => {
  dotenv.config();

  const id = process.env.USER_ID || '';
  const password = process.env.USER_PWD || '';

  const name_kk = process.env.TRAINEE_NAME_KK || '';
  const birth_kk = process.env.TRAINEE_BIRTH_KK || '';

  const name_sh = process.env.TRAINEE_NAME_SH || '';
  const birth_sh = process.env.TRAINEE_BIRTH_SH || '';

  const enterDate = process.env.ENTER_DATE || '';
  const className = process.env.CLASS_NAME as thecamp.SoldierClassName;
  const groupName = process.env.GROUP_NAME as thecamp.SoldierGroupName;
  const unitName = process.env.UNIT_NAME as thecamp.SoldierUnitName;

  await sendLetter({ id, password, name: name_kk, birth: birth_kk, enterDate, className, groupName, unitName });
  await sendLetter({ id, password, name: name_sh, birth: birth_sh, enterDate, className, groupName, unitName });
})();
