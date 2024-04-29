export const getList = () => {
    return [
      {
        id: 1,
        title: 'Chess',
        inputFormat:[
            'The first line contains two space-separated integers n and k, the length of the board\'s sides and the number of obstacles.',
            'The next line contains two space-separated integers rq and cq, the queen\'s row and column position.',
            'Each of the next k lines contains two space-separated integers r[i] and c[i], the row and column position of obstacles[i].'
        ]
      },
      {
        id: 2,
        title: 'Strings',
        inputFormat:[
            'A single line containing string t.',
        ]
      },
    ];
  };
  