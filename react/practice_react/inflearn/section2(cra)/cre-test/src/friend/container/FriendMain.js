import { getNextFriend } from '../../common/mockData';
import { actions, setValue } from "../state";
import { getAgeLimit, getShowLimit, getFriendsWithAgeLimit, getFriendsWithAgeShowLimit } from "../state/selector";
import FriendList from '../component/FriendList';
import NumberSelect from '../component/NumberSelect';
import { useSelector, useDispatch, shallowEqual } from 'react-redux';
import { MAX_AGE_LIMIT, MAX_SHOW_LIMIT } from '../common';

export default function FriendMain() {
  // const [friends, friends2] = useSelector(
  //   state => [state.friend.friends, state.friend.friends2],
  //   shallowEqual,
  // );
  const [
    ageLimit,
    showLimit,
    friendsWithAgeLimit,
    friendsWithAgeShowLimit,
  ] = useSelector( 
    state => [
      getAgeLimit(state),
      getShowLimit(state),
      getFriendsWithAgeLimit(state),
      getFriendsWithAgeShowLimit(state),
    ],
    shallowEqual,
  );
  //   state =>  {
  //   const { ageLimit, showLimit, friends } = state.friend;
  //   const friendsWithAgeLimit = friends.filter(item => item.age <= ageLimit);
  //   return [
  //     ageLimit, 
  //     showLimit, 
  //     friendsWithAgeLimit, 
  //     friendsWithAgeLimit.slice(0, showLimit)
  //   ];
  // }, shallowEqual);

  const dispatch = useDispatch();
  function onAdd() {
    const friend = getNextFriend();
    dispatch(actions.addFriend(friend));
  }
  console.log('Freind render');
  return (
    <div>
      <button onClick={onAdd}>친구  추가</button>
      <NumberSelect
        onChange={v => dispatch(actions.setValue('ageLimit', v))}
        value={ageLimit}
        options={AGE_LIMIT_OPTIONS}
        postfix="세 이하만 보기"
      />
      <FriendList friends={friendsWithAgeLimit} />
      <NumberSelect
        onChange={v => dispatch(actions.setValue('showLimit', v))}
        value={showLimit}
        options={SHOW_LIMIT_OPTIONS}
        postfix="명 이하만 보기 (연령 제한 적용)"
      />
      <FriendList friends={friendsWithAgeShowLimit} />
    </div>
  )
}

const AGE_LIMIT_OPTIONS = [15, 20, 25, MAX_AGE_LIMIT]
const SHOW_LIMIT_OPTIONS = [2, 4, 6, MAX_SHOW_LIMIT]