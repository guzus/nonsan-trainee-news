async function send({
  id,
  password,
  name,
  birth,
  enterDate,
  className,
  groupName,
  unitName,
}) {
  const soldier = new thecamp.Soldier(
    name,
    birth,
    enterDate,
    className,
    groupName,
    unitName,
    thecamp.SoldierRelationship.FRIEND
  );

  const cookies = await thecamp.login(id, password);
  await thecamp.addSoldier(cookies, soldier);
  const [trainee] = await thecamp.fetchSoldiers(cookies, soldier);

  const message = new thecamp.Message(
    `${
      new Date().getMonth() + 1
    }월 ${new Date().getDate()}일 종합 뉴스 (${new Date().getHours()}시 ${new Date().getMinutes()}분)`,
    await getNews(),
    trainee.getTraineeMgrSeq()
  );

  await thecamp.sendMessage(cookies, trainee, message);
}

export { sendLetter };
