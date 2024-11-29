const ScheduleTable = () => {
    return (
      <div className="container center mx-auto mt-10">
        <table className="table-auto border-collapse border border-gray-300 shadow-lg">
          <thead className="">
            <tr>
              <th className="border border-gray-300 px-4 py-2">Время</th>
              <th className="border border-gray-300 px-4 py-2">Понедельник</th>
              <th className="border border-gray-300 px-4 py-2">Вторник</th>
              <th className="border border-gray-300 px-4 py-2">Среда</th>
              <th className="border border-gray-300 px-4 py-2">Четверг</th>
              <th className="border border-gray-300 px-4 py-2">Пятница</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td className="border border-gray-300 px-4 py-2">08:00-09:00</td>
              <td className="border border-gray-300 px-4 py-2">А490</td>
              <td className="border border-gray-300 px-4 py-2">К190</td>
              <td className="border border-gray-300 px-4 py-2">В133</td>
              <td className="border border-gray-300 px-4 py-2">D420</td>
              <td className="border border-gray-300 px-4 py-2">Е330</td>
            </tr>
            <tr>
              <td className="border border-gray-300 px-4 py-2">09:10-10:10</td>
              <td className="border border-gray-300 px-4 py-2">К190</td>
              <td className="border border-gray-300 px-4 py-2">А490</td>
              <td className="border border-gray-300 px-4 py-2">М550</td>
              <td className="border border-gray-300 px-4 py-2">Е330</td>
              <td className="border border-gray-300 px-4 py-2">С315</td>
            </tr>
            <tr>
              <td className="border border-gray-300 px-4 py-2">10:20-11:20</td>
              <td className="border border-gray-300 px-4 py-2">D420</td>
              <td className="border border-gray-300 px-4 py-2">С001</td>
              <td className="border border-gray-300 px-4 py-2">М550</td>
              <td className="border border-gray-300 px-4 py-2">В133</td>
              <td className="border border-gray-300 px-4 py-2">А490</td>
            </tr>
            <tr>
              <td className="border border-gray-300 px-4 py-2">11:30-12:30</td>
              <td className="border border-gray-300 px-4 py-2">С315</td>
              <td className="border border-gray-300 px-4 py-2">D420</td>
              <td className="border border-gray-300 px-4 py-2">А490</td>
              <td className="border border-gray-300 px-4 py-2">М550</td>
              <td className="border border-gray-300 px-4 py-2">С001</td>
            </tr>
          </tbody>
        </table>
      </div>
    );
  };
  
  export default ScheduleTable;
  