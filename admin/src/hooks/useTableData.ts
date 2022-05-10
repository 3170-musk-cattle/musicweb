import { ref } from 'vue';

export interface ISimpleTableData {
  city: string;
  totalOrders: string;
}

export interface IPaginatedTableData {
  picture: string;
  name: string;
  role: string;
  created: string;
  status: string;
  statusColor: string;
}



export interface IWideTableData {
  name: string;
  email: string;
  title: string;
  title2: string;
  status: string;
  role: string;
}

export interface ArtistTableData {
  picture: string;
  name: string;
  type: string;
  
}

export function useTableData() {
  const simpleTableData = ref<ISimpleTableData[]>([
    { city: 'New York', totalOrders: '200,120' },
    { city: 'Manchester', totalOrders: '632,310' },
    { city: 'London', totalOrders: '451,110' },
    { city: 'Madrid', totalOrders: '132,524' },
  ]);

  const paginatedTableData = ref<IPaginatedTableData[]>([
    {
      picture:
        'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.2&w=160&h=160&q=80',
      name: 'Vera Carpenter',
      role: 'Admin',
      created: 'Jan 21, 2020',
      status: 'Active',
      statusColor: 'green',
    },
    {
      picture:
        'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.2&w=160&h=160&q=80',
      name: 'Blake Bowman',
      role: 'Editor',
      created: 'Jan 01, 2020',
      status: 'Active',
      statusColor: 'green',
    },
    {
      picture:
        'https://images.unsplash.com/photo-1540845511934-7721dd7adec3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.2&w=160&h=160&q=80',
      name: 'Dana Moore',
      role: 'Editor',
      created: 'Jan 10, 2020',
      status: 'Suspended',
      statusColor: 'orange',
    },
    {
      picture:
        'https://images.unsplash.com/photo-1522609925277-66fea332c575?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.2&h=160&w=160&q=80',
      name: 'Alonzo Cox',
      role: 'Admin',
      created: 'Jan 18, 2020',
      status: 'Inactive',
      statusColor: 'red',
    },
  ]);

  const wideTableData = ref<IWideTableData[]>(
    [...Array(10).keys()].map(() => ({
      name: 'John Doe',
      email: 'john@example.com',
      title: 'Software Engineer',
      title2: 'Web dev',
      status: 'Active',
      role: 'Owner',
    }))
  );
  
  

  return {
    simpleTableData,
    paginatedTableData,
    wideTableData,
  };
}

export function artTableData() {
  const artistTable = ref<ArtistTableData[]>(
    [
    {
      picture:
        '../img/logo.png',
      name: 'Czech',
      type: 'Individual',
    },
    {
      picture:
        '../img/logo.png',
      name: 'Czech Philharmonic Orchestra',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Czech/Gavin/Lindsey',
      type: 'Group',
    },

    {
      picture:
        '../img/logo.png',
      name: 'DJ Project',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'DJ Project/Giulia/Huiban Gabriel',
      type: 'Group',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Feint',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Feint/Leah Rye/Rameses B',
      type: 'Group',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Flipsyde',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Flipsyde/t.A.T.u.',
      type: 'Group',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Flo Rida',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Flo Rida/Robin Thicke/Verdine White',
      type: 'Group',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Flo Rida/Sage the Gemini',
      type: 'Group',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Flo Rida/Wynter Gordon',
      type: 'Group',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Gavin',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Gavin Greenaway',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Giulia',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Greyson Chance',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Huiban Gabriel',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Leah Rye',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Lindsey',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Lindsey Stirling',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Rameses B',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Robin Thicke',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Sage the Gemini',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Selena Gomez & The Scene',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Verdine White',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Wynter Gordon',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 'Yael Naïm',
      type: 'Individual',
    },

    {
      picture:
        '../img/logo.png',
      name: 't.A.T.u.',
      type: 'Individual',
    },
]);
  return artistTable;
}

export interface SongTableData {
  name: string;
  artist: string;
  album: string;
  comments: number;
}
export function songTableData() {
  const songTable = ref<SongTableData[]> ([
    {
      name: 'Round & Round',
      artist: 'Selena Gomez & The Scene',
      album: 'A Year Without Rain',
      comments: 2,
    },
    {
      name: 'Whiplash',
      artist: 'Selena Gomez & The Scene',
      album: 'When The Sun Goes Down (Deluxe Edition)',
      comments: 4,
    },

    {
      name: 'I Don\'t Like It, I Love It',
      artist: 'Flo Rida/Verdine White/Robin Thicke',
      album: 'My House',
      comments: 15,
    },

    {
      name: 'Game Time',
      artist: 'Flo Rida/Sage the Gemini',
      album: 'Game Time',
      comments: 15,
    },

    {
      name: 'Sugar',
      artist: 'Flo Rida/Wynter Gordon',
      album: 'R.O.O.T.S.',
      comments: 15,
    },

    {
      name: 'Stupid Goal',
      artist: 'Yael Naïm',
      album: 'She Was A Boy',
      comments: 4,
    },

    {
      name: 'Sleepwalking',
      artist: 'Lindsey Stirling',
      album: 'Artemis',
      comments: 3,
    },

    {
      name: 'Carol of the Bells',
      artist: 'Lindsey Stirling',
      album: 'Warmer In The Winter (Deluxe Version)',
      comments: 6,
    },

    {
      name: 'Unfriend You',
      artist: 'Greyson Chance',
      album: 'Hold On ‘Til The Night',
      comments: 15,
    },

    {
      name: 'London',
      artist: 'Greyson Chance',
      album: 'London',
      comments: 15,
    },

    {
      name: 'Today',
      artist: 'Yael Naïm',
      album: 'She Was A Boy',
      comments: 4,
    },

    {
      name: 'Falling Down',
      artist: 'Selena Gomez & The Scene',
      album: 'Kiss & Tell',
      comments: 1,
    },

    {
      name: 'Main Theme',
      artist: 'Lindsey/Gavin/Czech',
      album: 'Hans Zimmer - The Classics',
      comments: 15,
    },

    {
      name: 'Outlaw',
      artist: 'Selena Gomez & The Scene',
      album: 'When The Sun Goes Down (Deluxe Edition)',
      comments: 4,
    },

    {
      name: 'Falling Down',
      artist: 'DJ Project',
      album: 'Povestea Mea',
      comments: 4,
    },
    {
      name: 'Sparks',
      artist: 't.A.T.u.',
      album: 'Waste Management',
      comments: 4,
    },

    {
      name: 'Show Me Love',
      artist: 't.A.T.u.',
      album: '200 KM/H In The Wrong Lane',
      comments: 2,
    },

    {
      name: 'Nu (Extended Version)',
      artist: 'DJ Project/Giulia/Huiban Gabriel',
      album: 'Nu',
      comments: 1,
    },

    {
      name: 'Let U Go',
      artist: 'DJ Project',
      album: 'In the Club',
      comments: 4,
    },

    {
      name: 'Perfect Enemy',
      artist: 't.A.T.u.',
      album: 'Dangerous and Moving',
      comments: 4,
    },

    {
      name: 'Starseed (Rameses B Remix)',
      artist: 'Feint/Rameses B/Leah Rye',
      album: 'Weavers',
      comments: 8,
    },

    {
      name: 'Believe in Goodbyes',
      artist: 't.A.T.u.',
      album: 'Believe in Goodbyes',
      comments: 1,
    },

    {
      name: 'Fly on the Wall',
      artist: 't.A.T.u.',
      album: 'Happy Smiles',
      comments: 2,
    },

    {
      name: 'All the thing she said',
      artist: 't.A.T.u.',
      album: '',
      comments: 2,
    },

    {
      name: 'Show Me Love (Radio Edit)',
      artist: 't.A.T.u.',
      album: 't.A.T.u. - The Best',
      comments: 5,
    },

    {
      name: 'Not Gonna Get Us',
      artist: 't.A.T.u.',
      album: '200 KM/H In The Wrong Lane',
      comments: 2,
    },

    {
      name: 'Don\'t Regret',
      artist: 't.A.T.u.',
      album: 'Waste Management (Explicit)',
      comments: 4,
    },

    {
      name: 'All The Things She Said (Original Album Version|Edited)',
      artist: 't.A.T.u.',
      album: 't.A.T.u. - The Best',
      comments: 1,
    },

    {
      name: 'Loves Me Not (Guena G Remix Edit)',
      artist: 't.A.T.u.',
      album: 't.A.T.u. - The Best',
      comments: 9,
    },

    {
      name: 'You and I',
      artist: 't.A.T.u.',
      album: 'Happy Smiles',
      comments: 4,
    },

    {
      name: 'Gomenasai',
      artist: 't.A.T.u.',
      album: 'Dangerous and Moving',
      comments: 14,
    },

    {
      name: '30 Minutes',
      artist: 't.A.T.u.',
      album: '200 Po Vstrechnoy',
      comments: 15,
    },

    {
      name: 'All The Things She Said',
      artist: 't.A.T.u.',
      album: '200 KM/H In The Wrong Lane',
      comments: 15,
    },

    {
      name: 'All About Us',
      artist: 't.A.T.u.',
      album: 'Dangerous and Moving',
      comments: 10,
    },

    {
      name: 'Loves Me Not',
      artist: 't.A.T.u.',
      album: 'Dangerous and Moving',
      comments: 15,
    },
    {
      name: 'We All Want The Same Thing',
      artist: 'push baby',
      album: 'This Is Acoustic (Live Session)',
      comments: 2,
    },

    {
      name: 'thor',
      artist: 'push baby',
      album: 'thor',
      comments: 4,
    },

    {
      name: 'Speakerphone',
      artist: 'push baby',
      album: 'This Is Acoustic (Live Session)',
      comments: 1,
    },

    {
      name: 'Me And My Broken Heart (Pnau Remix)',
      artist: 'push baby',
      album: 'Me And My Broken Heart (Remixes)',
      comments: 4,
    },

    {
      name: 'Problem',
      artist: 'push baby',
      album: '最新热歌慢摇84',
      comments: 4,
    },

    {
      name: 'Me and My Broken Heart (Live at New Year\'s Rockin\' Eve 2015)',
      artist: 'push baby',
      album: '',
      comments: 1,
    },

    {
      name: 'Me And My Broken Heart',
      artist: 'push baby',
      album: 'This Is Acoustic (Live Session)',
      comments: 3,
    },

    {
      name: 'Me And My Broken Heart (Lovelife Remix)',
      artist: 'push baby',
      album: 'Me And My Broken Heart (Remixes)',
      comments: 3,
    },

    {
      name: 'Me and My Broken Heart (不插电版)',
      artist: 'push baby',
      album: '',
      comments: 4,
    },

    {
      name: 'Whole',
      artist: 'push baby',
      album: 'Let The Road',
      comments: 8,
    },

    {
      name: 'Beautiful Excuses',
      artist: 'push baby',
      album: 'Let The Road',
      comments: 7,
    },

    {
      name: 'Hola',
      artist: 'Flo Rida/Maluma',
      album: 'Hola',
      comments: 15,
    },

    {
      name: 'Make Out',
      artist: 'push baby',
      album: 'Let The Road',
      comments: 12,
    },

    {
      name: 'Sorry To Interrupt',
      artist: 'Jessie J/Jhené Aiko/push baby',
      album: 'Sorry To Interrupt',
      comments: 11,
    },

    {
      name: 'I Like Girls',
      artist: 'push baby',
      album: 'Let The Road',
      comments: 5,
    },

    {
      name: 'Zi-Zi\'s Journey',
      artist: 'Lindsey Stirling',
      album: 'Lindsey Stirling',
      comments: 15,
    },

    {
      name: 'We All Want The Same Thing',
      artist: 'push baby',
      album: 'Me And My Broken Heart',
      comments: 15,
    },

    {
      name: 'Hotel Ceiling',
      artist: 'push baby',
      album: 'Me And My Broken Heart',
      comments: 15,
    },
  ]);
  return songTable;
}