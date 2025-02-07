const InputBox = () => {
    return (
        <div className="p-8 pb-0 flex justify-left relative">
            <input
                type="text"
                placeholder="ANSWER"
                className="w-full bg-gray-100 border-4 border-black rounded-lg p-2 md:p-4 font-pixel text-black"
            />
            {/* In the future, this dropdown component will be dynamically rendered! */}
            <div className="absolute top-full mt-4 bg-gray-100 border-4 border-black rounded-lg p-2 md:p-4 font-pixel text-black">
                <ul className="max-h-56 overflow-auto">
                    <li className="hover:bg-gray-200 cursor-pointer">Darius Garland</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Donovan Mitchell</li>
                    <li className="hover:bg-gray-200 cursor-pointer">De'Andre Hunter</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Evan Mobley</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Jarrett Allen</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Darius Garland</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Donovan Mitchell</li>
                    <li className="hover:bg-gray-200 cursor-pointer">De'Andre Hunter</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Evan Mobley</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Jarrett Allen</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Darius Garland</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Donovan Mitchell</li>
                    <li className="hover:bg-gray-200 cursor-pointer">De'Andre Hunter</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Evan Mobley</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Jarrett Allen</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Darius Garland</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Donovan Mitchell</li>
                    <li className="hover:bg-gray-200 cursor-pointer">De'Andre Hunter</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Evan Mobley</li>
                    <li className="hover:bg-gray-200 cursor-pointer">Jarrett Allen</li>
                </ul>
            </div>
        </div>
    );
};

export default InputBox;
